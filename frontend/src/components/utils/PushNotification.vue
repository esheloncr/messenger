<template>
<div class="notification-container" v-show="isShown === true">
  <div class="notification-title">
    <span class="notification-title__text">
      {{ title }}
    </span>
  </div>
  <div class="notification-body">
    <p class="notification-body__text">
      {{ body }}
    </p>
  </div>
</div>
</template>

<script>
export default {
  name: "PushNotification",
  props: ['title', 'body'],
  data() {
    return {
      isShown: true
    }
  },
  created() {
    setTimeout(() => {
      this.isShown = false;
    }, 3000);
  },
}
</script>

<style scoped>
  body {
    overflow-x: hidden;
  }
  .notification-container {
    width: 250px;
    border-radius: 6px;
    background: white;
    padding: 10px;
    animation: scroll 0.3s;
    position: absolute;
  }
  .notification-container span, .notification-container p {
    font-size: 15px;
    color: black;
  }
  @keyframes scroll {
    0% {
      transform: translate3d(-1800px, 0, 0);
    }
    100% {
      transform: translate3d(0, 0, 0);
    }
  }
</style>