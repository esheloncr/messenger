<template>
  <Navbar/>
  <RegistrationForm/>
</template>

<script>
import Navbar from "@/components/Navbar.vue";
import RegistrationForm from "@/components/forms/RegistrationForm.vue";
export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: "Registration",
  components: {
    Navbar,
    RegistrationForm
  }
}
</script>

<style scoped>

</style>