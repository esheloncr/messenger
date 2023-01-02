<template>
  <PushNotification v-if="hasErrors" title="Invalid registration data" body="Invalid data"/>
  <!-- TODO: Add fields validation and error-handler -->
  <form @submit="register">
    <div class="container">
      <h1>Sign up</h1>
      <div class="controls">
        <div class="field username-input-wrapper">
          <label for="username">Username</label>
          <input type="text" name="username" v-model="username" class="username__input" :class="{ 'has-errors': hasErrors }" required>
        </div>
        <div class="field first-name-input-wrapper">
          <label for="first-name">First name</label>
          <input type="text" name="first-name" v-model="firstName" class="first_name__input" :class="{ 'has-errors': hasErrors }" required>
        </div>
        <div class="field last-name-input-wrapper">
          <label for="last-name">Last name</label>
          <input type="text" name="last-name" v-model="lastName" class="last_name__input" :class="{ 'has-errors': hasErrors }" required>
        </div>
        <div class="field birth-date-input-wrapper">
          <label for="birth-date">Date of birth</label>
          <DatePicker v-model="birthDate" format="yyyy-MM-dd" :start-date="new Date(2000, 0, 1)" required :class="{ 'has-errors': hasErrors }" :enable-time-picker="false"/>
        </div>
        <div class="field password-input-wrapper">
          <label for="password">Password</label>
          <input type="password" name="password" v-model="password" class="password__input" :class="{ 'has-errors': hasErrors }" required>
        </div>
        <div class="field password-input-wrapper">
          <label for="password2">Repeat password</label>
          <input type="password" name="password2" v-model="password2" class="password__input" :class="{ 'has-errors': hasErrors }" required>
        </div>
        <input type="submit" value="Sign up" class="authentication__submit">
      </div>
    </div>
  </form>
</template>

<script>
import PushNotification from "@/components/utils/PushNotification.vue";
import DatePicker from '@vuepic/vue-datepicker';
import '@vuepic/vue-datepicker/dist/main.css';
import moment from "moment";

export default {
  name: "RegistrationForm",
  components: {
    PushNotification,
    DatePicker
  },
  data() {
    return {
      username: '',
      firstName: '',
      lastName: '',
      birthDate: '',
      password: '',
      password2: '',
      hasErrors: false,
    }
  },
  methods: {
    register(event) {
      event.preventDefault();
      const username = this.username;
      const password = this.password;
      const password2 = this.password2;
      const birthDate = moment(this.birthDate).format("YYYY-MM-DD")
      const first_name = this.firstName;
      const lastName = this.lastName;
      const registerUri = 'http://localhost:8000/api/v1/users/create/';
      const data = {
        username: username,
        password: password,
        password2: password2,
        first_name: first_name,
        last_name: lastName,
        birth_date: birthDate
      }
      this.axios
          .post(registerUri, data)
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
  }
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
  .field {
    display: flex;
    flex-direction: column;
    gap: 5px;
    margin-bottom: 10px;
  }
  .field > input {
    padding: 10px;
    border-radius: 5px;
    border-width: 0;
    background-color: #ffffff38;
    color: white;
  }
  .dp__theme_light {
    --dp-background-color: #ffffff38;
    --dp-text-color: white;
  }
  .authentication__submit {
    margin-top: 5px;
    width: 100%;
    border-radius: 5px;
    padding: 10px;
    background-color: #6663035c;
    color: #ffffff8a;
  }
  .authentication__submit:hover {
    cursor: pointer;
  }
  .field input.has-errors {
    border-color: red;
    border-width: 1px;
  }
</style>