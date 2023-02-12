import { createApp } from 'vue'
import App from '@/App.vue'
import router from "@/router";
import VueAxios from "vue-axios";
import axios from "axios";
import moment from "moment";

const localeMixin = {
    methods: {
        gettext(text) {
            return window.gettext(text);
        },
        formatDate(date, format="DD-MM-YYYY"){
            return moment(date).format(format);
        }
    }
}

const app = createApp(App);
app.use(router);
app.use(VueAxios, axios);
app.mixin(localeMixin);
app.mount("#app");
