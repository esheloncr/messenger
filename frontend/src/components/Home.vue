<template>
  <Navbar/>
  <UserList/>
</template>

<script>
import Navbar from "@/components/Navbar.vue";
import UserList from "@/components/user/UserList.vue";
export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: "Home",
  components: {
    Navbar,
    UserList
  },
}
</script>

<style scoped>

</style>