<template>
  <div>
    <h1 class="mb-2">Туры</h1>
    <p class="mb-4">Список актуальных туров, выбирайте тот, что вам по душе!</p>
    <router-link :to="'/tours_filter/'">
      Найти то, что точно подойдет
    </router-link>
    <hr/>
    <ToursList />
    <v-pagination v-model="toursPagination.page" :length="toursPagination.pages" @input="next"></v-pagination>
  </div>
</template>

<script>
import ToursList from "@/components/ToursList";
import {mapGetters} from "vuex";

export default {
  name: "HomePage",
  components: {ToursList},
  computed: {
    ...mapGetters({
      toursPagination: 'toursPagination'
    })
  },
  methods: {
    next(page) {
      this.$store.dispatch('toursList', page)
    }
  },
  mounted: function() {
    this.$store.dispatch('toursList')
  },
}
</script>

<style scoped>

</style>