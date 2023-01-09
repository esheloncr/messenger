<template>
  <h1>User List</h1>
  <div class="container">
    <UserListItem v-for="item in userList" :key="item.age" :fullName="item.fullName" :age="item.age" :avatar="item.avatar" :birthDate="item.birthDate"/>
  </div>
</template>

<script>
import UserListItem from "@/components/user/UserListItem.vue";
export default {
  name: "UserList",
  components: {
    UserListItem
  },
  data(){
    return {
      userList: []
    }
  },
  methods: {
    getUserList(){
      const requestUri = 'http://localhost:8000/api/v1/users/';
      this.axios
          .get(requestUri)
          .then((response) => {
            response.data.map(item => {
              this.userList.push({
                fullName: item.full_name,
                age: item.age,
                avatar: item.avatar_resized,
                birthDate: item.birth_date
              });
            })
          })
    }
  },
  mounted() {
    this.getUserList();
  }
}
</script>

<style scoped>

</style>