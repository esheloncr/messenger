<template>
  <div class="navbar-container">
    <div class="nav-buttons" :class="{ 'centered': this.isAuthenticated() }">
      <router-link to="/" class="home-page__link">{{ this.gettext("Home page") }}</router-link>
      <router-link to="/login" class="sign-in__link" v-if="isAllowedToShowAuthenticationLink('login')">{{ this.gettext("Sign in") }}</router-link>
      <router-link to="/registration" class="sign-up__link" v-if="isAllowedToShowAuthenticationLink('registration')">{{ this.gettext("Sign up") }}</router-link>
      <a class="logout__button" @click="logout" v-if="isAuthenticated()">{{ this.gettext("Logout") }}</a>
    </div>
    <div class="user-info-wrapper" v-if="this.isAuthenticated()">
      <UserNavbarMenu/>
    </div>
  </div>
</template>

<script>
import {useRoute} from "vue-router";
import UserNavbarMenu from "@/components/user/UserNavbarMenu";

const routes = {
  login: 'login',
  registration: 'registration',
  home: 'index'
}
export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: "Navbar",
  components: {
    UserNavbarMenu
  },
  methods: {
    isAllowedToShowAuthenticationLink(route){
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
.nav-buttons.centered, .user-info-wrapper {
  margin-left: auto;
}
.nav-buttons.centered .home-page__link {
  margin-left: 150px;
}
</style>