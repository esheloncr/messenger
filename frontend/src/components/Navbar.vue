<template>
  <div class="navbar-container">
    <router-link to="/" class="home-page__link">Home page</router-link>
    <router-link to="/login" class="sign-in__link" v-if="isAllowedToShowLink('login')">Sign in</router-link>
    <router-link to="/registration" class="sign-up__link" v-if="isAllowedToShowLink('registration')">Sign up</router-link>
    <a class="logout__button" @click="logout" v-if="isAuthenticated()">Logout</a>
  </div>
</template>

<script>
import {useRoute} from "vue-router";

const routes = {
  login: 'login',
  registration: 'registration',
  home: 'index'
}
export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: "Navbar",
  methods: {
    isAllowedToShowLink(route){
      const routeName = routes[route];
      const currentRoute = useRoute().name;
      return !(routeName === currentRoute) && !this.isAuthenticated();
    },
    logout() {
      localStorage.removeItem('token');
      this.token = '';
    },
  },
  data(){
    return {
      token: localStorage.getItem('token'),
      isAuthenticated: () => {
        return Boolean(this.token);
      }
    }
  },
}
</script>

<style scoped>
.logout__button:hover {
  cursor: pointer;
}
</style>