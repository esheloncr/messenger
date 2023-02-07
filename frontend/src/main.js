import { createApp } from 'vue'
import App from '@/App.vue'
import router from "@/router";
import VueAxios from "vue-axios";
import axios from "axios";

const getTextMixin = {
    methods: {
        gettext(text) {
            return window.gettext(text);
        }
    }
}

const app = createApp(App);
app.use(router);
app.use(VueAxios, axios);
app.mixin(getTextMixin);
app.mount("#app");
