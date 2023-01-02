import { createRouter, createWebHashHistory } from "vue-router";
import Home from "@/components/Home.vue";
import Login from "@/components/Login.vue";

export default createRouter({
    routes: [
        { path: '/', component: Home },
        { path: '/login', component: Login }
    ],
    history: createWebHashHistory()
});