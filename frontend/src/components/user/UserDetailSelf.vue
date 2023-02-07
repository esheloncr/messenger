<template>
  <Navbar/>
  <div class="content-wrapper">
    <img :src="`http://localhost:8000${this.avatar}`" alt="user-avatar" class="avatar">
    <div class="info-wrapper">
      <div class="full-name">
        <span>{{ firstName }} {{ lastName }}</span>
      </div>
      <div class="birth-date">
        <span>{{ this.gettext("Birthdate") }}: {{ birthDate }} ({{ this.gettext("Age") }}: {{ age }})</span>
      </div>
    </div>
  </div>
</template>

<script>
import Navbar from "@/components/Navbar";

export default {
  name: "UserDetailSelf",
  components: {
    Navbar
  },
  methods: {
    getUserData() {
      const requestUri = 'http://localhost:8000/api/v1/users/me';
      const token = localStorage.getItem('token');
      const headers = {
        'Authorization': `Token ${token}`
      };
      this.axios
          .get(requestUri, {
            headers: headers
          })
          .then((response) => {
            const data = response.data.full;
            this.username = data.username;
            this.firstName = data.first_name;
            this.lastName = data.last_name;
            this.birthDate = data.birth_date;
            this.age = data.age;
            this.avatar = data.avatar_resized;
          })
    }
  },
  mounted() {
    this.getUserData();
  },
  data() {
    return {
      username: '',
      firstName: '',
      lastName: '',
      birthDate: '',
      age: '',
      avatar: ''
    }
  }
}
</script>

<style scoped>
  .content-wrapper {
    display: flex;
    gap: 30px;
    align-items: center;
    justify-content: center;
    margin-top: 50px;
    margin-left: 130px;
  }
  .content-wrapper .avatar {
    border-radius: 50px;
  }
  .content-wrapper .full-name {
    text-transform: capitalize;
  }
</style>