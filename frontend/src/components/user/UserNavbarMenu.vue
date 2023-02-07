<template>
<div class="user-navbar-info-wrapper">
  <img :src="`http://localhost:8000${userAvatar}`" alt="user-avatar" class="user-navbar__image">
  <router-link to="/users/me" class="user-navbar-username">{{ username }}</router-link>
</div>
</template>

<script>
export default {
  name: "UserNavbarMenu",
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
            const data = response.data.short;
            this.username = data.username;
            this.userAvatar = data.avatar_resized;
          })
    }
  },
  data() {
    return {
      username: '',
      userAvatar: ''
    }
  },
  mounted() {
    this.getUserData();
  }
}
</script>

<style scoped>
.user-navbar-info-wrapper {
  display: flex;
  flex-direction: row;
  flex-wrap: nowrap;
  gap: 15px;
  align-items: center;
}
.user-navbar__image {
  border-radius: 50px;
}
</style>