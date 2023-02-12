import { createRouter, createWebHashHistory } from "vue-router";
import Home from "@/components/Home.vue";
import Login from "@/components/authentication/Login.vue";
import Registration from "@/components/authentication/Registration.vue";
import UserDetailSelf from "@/components/user/UserDetailSelf";

const routes = [
    { path: '/', component: Home, name: 'index' },
    { path: '/login', component: Login, name: 'login' },
    { path: '/registration', component: Registration, name: 'registration' },
    { path: '/users/me', component: UserDetailSelf, name: 'userDetailSelf' }
]
export default createRouter({
    routes,
    history: createWebHashHistory()
});