<template>
  <Navbar/>
  <LoginForm/>
</template>

<script>
import LoginForm from "@/components/forms/LoginForm.vue";
import Navbar from "@/components/Navbar.vue";

export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: "Login",
  components: {
    LoginForm,
    Navbar
  }
}
</script>

<style scoped>

</style>