# flake8: noqa
from django.core.management.commands.makemessages import (
    Command as DefaultMakeMessagesCommand,
)
from django.core.management.commands.makemessages import *


class Command(DefaultMakeMessagesCommand):
    def handle(self, *args, **options):
        data = {
            "locale": ['en'],
            "domain": "djangojs",
            "ignore_patterns": ["node_modules/*", "venv/*"],
            "extensions": ["vue", "js"],
        }
        options.update(data)
        super(Command, self).handle(*args, **options)

    def process_locale_dir(self, locale_dir, files):
        """
        Extract translatable literals from the specified files, creating or
        updating the POT file for a given locale directory.

        Use the xgettext GNU gettext utility.
        """
        build_files = []
        for translatable in files:
            if self.verbosity > 1:
                self.stdout.write(
                    "processing file %s in %s"
                    % (translatable.file, translatable.dirpath)
                )
            if self.domain not in ("djangojs", "django"):
                continue
            build_file = self.build_file_class(self, self.domain, translatable)
            try:
                build_file.preprocess()
            except UnicodeDecodeError as e:
                self.stdout.write(
                    "UnicodeDecodeError: skipped file %s in %s (reason: %s)"
                    % (
                        translatable.file,
                        translatable.dirpath,
                        e,
                    )
                )
                continue
            except BaseException:
                # Cleanup before exit.
                for build_file in build_files:
                    build_file.cleanup()
                raise
            build_files.append(build_file)

        if self.domain == "djangojs":
            args = [
                "xgettext",
                "-d",
                self.domain,
                "--keyword=_",
                "--keyword=gettext",
                "--keyword=$gettext",
                "--output=-",
            ]

        input_files = [bf.work_path for bf in build_files]
        with NamedTemporaryFile(mode="w+") as input_files_list:
            input_files_list.write("\n".join(input_files))
            input_files_list.flush()
            args.extend(["--files-from", input_files_list.name])
            args.extend(self.xgettext_options)
            msgs, errors, status = popen_wrapper(args)

        if errors:
            if status != STATUS_OK:
                for build_file in build_files:
                    build_file.cleanup()
                raise CommandError(
                    "errors happened while running xgettext on %s\n%s"
                    % ("\n".join(input_files), errors)
                )

        if msgs:
            if locale_dir is NO_LOCALE_DIR:
                for build_file in build_files:
                    build_file.cleanup()
                file_path = os.path.normpath(build_files[0].path)
                raise CommandError(
                    "Unable to find a locale path to store translations for "
                    "file %s. Make sure the 'locale' directory exists in an "
                    "app or LOCALE_PATHS setting is set." % file_path
                )
            for build_file in build_files:
                msgs = build_file.postprocess_messages(msgs)
            potfile = os.path.join(locale_dir, "%s.pot" % self.domain)
            write_pot_file(potfile, msgs)

        for build_file in build_files:
            build_file.cleanup()
