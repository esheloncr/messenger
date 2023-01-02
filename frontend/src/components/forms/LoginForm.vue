<template>
  <div class="container">
    <h1>Sign in</h1>
    <div class="controls">
      <div class="username-input-wrapper">
        <label for="username">Username</label>
        <input type="text" name="username" v-model="username" class="username__input">
      </div>
      <div class="password-input-wrapper">
        <label for="password">Password</label>
        <input type="password" name="password" v-model="password" class="password__input">
      </div>
      <input type="submit" value="Sign in" @click="authenticate" class="authentication__submit">
    </div>
  </div>
</template>

<script>

export default {
  name: "LoginForm",
  data() {
    return {
      username: '',
      password: '',
      token: ''
    }
  },
  methods: {
    authenticate() {
      const username = this.username;
      const password = this.password;
      const loginUri = 'http://localhost:8000/api/v1/users/login/';
      const data = {
        username: username,
        password: password
      }
      this.axios
          .post(loginUri, data)
          .then((response) => {
            this.token = response.data.token;
            localStorage.setItem('token', this.token);
            this.$router.push('/');
          })
    }
  },
}
</script>

<style scoped>
  .container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    min-height: 50vh;
  }
  .username-input-wrapper, .password-input-wrapper {
    display: flex;
    flex-direction: column;
    gap: 5px;
    margin-bottom: 10px;
  }
  .username-input-wrapper > .username__input, .password-input-wrapper > .password__input {
    border-radius: 5px;
    border-width: 0;
    height: 25px;
    background-color: #ffffff38;
    color: white;
  }
  .username-input-wrapper > .username__input:-webkit-autofill, .password-input-wrapper > .password__input:-webkit-autofill {
    background-color: yellow;
  }
  .authentication__submit {
    margin-top: 5px;
    width: 100%;
    border-radius: 5px;
    height: 25px;
    background-color: #6663035c;
    color: #ffffff8a;
  }
  .authentication__submit:hover {
    cursor: pointer;
  }
</style>