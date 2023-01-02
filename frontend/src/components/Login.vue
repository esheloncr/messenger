<template>
  <router-link to="/" class="home-page__link">Home page</router-link>
  <LoginForm/>
</template>

<script>
import LoginForm from "@/components/forms/LoginForm.vue";

export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: "Login",
  components: {
    LoginForm
  }
}
</script>

<style scoped>

</style>