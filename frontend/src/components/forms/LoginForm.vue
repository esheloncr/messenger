<template>
  <PushNotification v-if="hasErrors" title="Invalid credentials" body="Invalid username or password"/>
  <form @submit="authenticate">
    <div class="container">
      <h1>Sign in</h1>
      <div class="controls">
        <div class="username-input-wrapper">
          <label for="username">{{ this.gettext("Username") }}</label>
          <input type="text" name="username" v-model="username" class="username__input" :class="{ 'has-errors': hasErrors }">
        </div>
        <div class="password-input-wrapper">
          <label for="password">{{ this.gettext("Password") }}</label>
          <input type="password" name="password" v-model="password" class="password__input" :class="{ 'has-errors': hasErrors }">
        </div>
        <input type="submit" value="Sign in" class="authentication__submit">
      </div>
    </div>
  </form>
</template>

<script>
import PushNotification from "@/components/utils/PushNotification.vue";
export default {
  name: "LoginForm",
  data() {
    return {
      username: '',
      password: '',
      token: '',
      hasErrors: false
    }
  },
  components: {
    PushNotification
  },
  methods: {
    authenticate(event) {
      event.preventDefault();
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
          .catch((error) => {
            const statusCode = error.response.status;
            if (statusCode === 400) {
              this.hasErrors = true;
              setTimeout(() => {
                this.hasErrors = false;
              }, 3000);
            }
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
  .username-input-wrapper > .username__input.has-errors, .password-input-wrapper > .password__input.has-errors {
    border-color: red;
    border-width: 1px;
  }
</style>