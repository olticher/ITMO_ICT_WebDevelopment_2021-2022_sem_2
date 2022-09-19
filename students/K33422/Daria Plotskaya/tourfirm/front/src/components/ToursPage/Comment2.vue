<template>
  <div>
    <b-list-group-item class="mb-5">
      <div class="d-flex align-items-center">
        <b-avatar class="mr-3"></b-avatar>
        <span class="mr-auto">{{ name }}</span>
      </div>
      <p class="text-start">{{ text }}</p>
      <span class="d-flex align-items-center">
      <b-icon-star-fill v-for="index in stars" :key="index" class="d-flex flex-row"/>
    <span class="ml-5">{{ `${stars}/10` }}</span>
    </span>
    </b-list-group-item>
  </div>
</template>

<script>
export default {
  name: "Comment2",
  props: ['name', 'text', 'stars']
}
</script>

<style scoped>

</style>