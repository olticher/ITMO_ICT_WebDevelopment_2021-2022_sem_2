<template>
  <div>
    <h1 class="mb-2">Туры</h1>
    <p class="mb-4">Список актуальных туров, выбирайте тот, что вам по душе!</p>
    <div class="filters mb-4 ">
      <label>
        Минимальная цена:
        <b-input v-model="min" @change="changeMin"/>
      </label>
      <label>
        Максимальная цена:
        <b-input v-model="max" @change="changeMax"/>
      </label>
      <div class="check-field mt-6 ml-10">
        Сортировать по цене:
        <v-checkbox v-model="isSorted" @change="setIsSorted" class="mt-6"/>
      </div>
    </div>
    <ToursList/>
    <v-pagination v-if="$store.state.toursList" v-model="toursPagination.page" :length="toursPagination.pages" @input="getData"></v-pagination>
  </div>
</template>

<script>
import ToursList from "@/components/ToursList";
import {mapGetters} from "vuex";

export default {
  name: "HomeFilterPage",
  components: {ToursList},
  data() {
    return {
      min: null,
      max: null,
      isSorted: false
    }
  },
  computed: {
    ...mapGetters({
      toursPagination: 'toursPagination'
    })
  },
  methods: {
    changeMin(value) {
      this.min = value
    },
    changeMax(value) {
      this.max = value
    },
    setIsSorted(value) {
      this.isSorted = value
    },
    getData(page) {
      if (this.min !== null && this.max !== null) {
        this.$store.dispatch('toursPriceRange', {page: page, min: this.min, max: this.max, isSorted: this.isSorted})
      }
    },
  },
  mounted: function() {
    this.$store.commit('setTours', null)
  },
  watch: {
    min: function() {
        this.getData()
    },
    max: function() {
        this.getData()
    },
    isSorted: function() {
        this.getData()
    },
  }
}
</script>

<style scoped>
.filters {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 10px;
}

.check-field {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 10px;
}
</style>
