<template>
  <h1>Messenger</h1>
  <button @click="logout" v-show="isAuthenticated() === true">Logout</button>
  <router-link to="/login" v-show="isAuthenticated() === false">Login page</router-link>
</template>

<script>

export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: "Home",
  data() {
    return {
      token: localStorage.getItem('token'),
      isAuthenticated: function (){
        return Boolean(this.token);
      }
    }
  },
  methods: {
    logout() {
      localStorage.removeItem('token');
      this.token = '';
    }
  }
}
</script>

<style scoped>

</style>