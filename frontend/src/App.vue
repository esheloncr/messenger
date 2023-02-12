<template>
  <router-view></router-view>
</template>

<script>

export default {

}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat&display=swap');
html {
  height: 100%;
}
body {
  background-image: url("./assets/main_background.jpg");
  background-repeat: no-repeat;
  animation: scroll linear 45s infinite;
}
* {
  font-family: "Montserrat";
}
@keyframes scroll {
  0% {
    background-position-y: 0;
  }
  25% {
    background-position-y: 25%;
  }
  50% {
    background-position-y: 50%
  }
  75% {
    background-position-y: 25%;
  }
  100% {
    background-position-y: 0;
  }
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: white;
  margin-top: 60px;
  padding: 20px;
}
a {
  text-decoration: none;
  color: white;
}
.home-page__link {
  color: white;
  text-decoration: none;
}
.navbar-container {
  display: flex;
  margin: 0 auto;
  justify-content: center;
  align-items: center;
}
.navbar-container .nav-buttons {
  display: flex;
  gap: 10px;
  padding: 10px;
}
.sign-in__link, .sign-up__link {
  text-decoration: none;
  color: white;
}
</style>
