<template>
  <div class="user-item">
    <div class="image-wrapper">
      <img :src="`http://localhost:8000${avatar}`" class="img-responsive">
    </div>
    <div class="user-info-wrapper">
      <div class="name-wrapper">
        <span>{{ fullName }}</span>
      </div>
      <div class="age-wrapper">
        <span>Birth date: {{ this.formatDate(birthDate) }} (age: {{ age }})</span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "UserListItem",
  props: ['fullName', 'age', 'avatar', 'birthDate'],
}
</script>

<style scoped>
  .img-responsive {
    border-radius: 50px;
  }
  .user-item {
    display: flex;
    justify-content: center;
    gap: 20px;
    margin-bottom: 20px;
  }
  .user-info-wrapper {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    gap: 10px;
  }
  .user-info-wrapper .name-wrapper {
    text-transform: capitalize;
  }
</style>