<template>
  <router-view></router-view>
</template>

<script>

export default {

}
</script>

<style>
html {
  height: 100%;
}
body {
  background-image: url("./assets/main_background.jpg");
  background-repeat: no-repeat;
  animation: scroll linear 45s infinite;
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
}
.home-page__link {
  color: white;
  text-decoration: none;
}
.navbar-container {
  display: flex;
  gap: 10px;
  margin: 0 auto;
  justify-content: center;
}
.sign-in__link, .sign-up__link {
  text-decoration: none;
  color: white;
}
</style>
