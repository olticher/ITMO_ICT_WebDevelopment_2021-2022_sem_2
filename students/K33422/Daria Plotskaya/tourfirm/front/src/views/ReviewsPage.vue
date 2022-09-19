<template>
  <div class="d-flex flex-column align-center mt-10">
    <h1 class="mb-10">Отзывы</h1>
    <div class="d-flex align-items-center  gap-5 mb-10">
      <span>Сортировать: </span>
      <b-button @click="makeAscending">По рейтингу
        <b-icon-arrow-up/>
      </b-button>
      <b-button @click="makeDescending">
        По рейтингу
        <b-icon-arrow-down/>
      </b-button>
    </div>
    <div v-for="(el, index) in reviewsList" :key="index">
      <Review :name="el.name" :text="el.text" :stars="el.stars"/>
    </div>
    <v-pagination v-if="$store.state.reviewsList" v-model="reviewsPagination.page" :length="reviewsPagination.pages"
                  @input="next"></v-pagination>
  </div>
</template>

<script>
import {mapGetters} from "vuex";
import Review from "@/components/ToursPage/Review";

export default {
  name: "ReviewsPage",
  components: {Review},
  mounted() {
    this.$store.dispatch('getReviews', {tour: this.$route.params.id})
  },
  data() {
    return {
      ordering: 'reservation'
    }
  },
  computed: {
    ...mapGetters({
      reviewsList: 'reviewsList',
      reviewsPagination: 'reviewsPagination',
    }),
  },
  watch: {
    ordering: function() {
      const payload = {
        page: this.reviewsPagination.page,
        ordering: this.ordering,
        tour: this.$route.params.id
      }
      this.$store.dispatch('getReviews', payload)
    },
  },
  methods: {
    next(page) {
      const payload = {
        page: page,
        ordering: this.ordering,
        tour: this.$route.params.id
      }
      this.$store.dispatch('getReviews', payload)
    },
    makeAscending() {
      this.ordering = 'stars'
    },
    makeDescending() {
      this.ordering = '-stars'
    },
  },
}
</script>

<style scoped>

</style>