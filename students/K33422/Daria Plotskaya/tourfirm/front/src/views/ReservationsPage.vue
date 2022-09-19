<template>
  <div>
    <h1 class="mb-10">Заказы</h1>

    <div class="filters mb-10">
      <label>
        Место:
        <b-input v-model="destination" @change="changeDestination"/>
      </label>
      <label>
        Количество человек:
        <b-input v-model="count" @change="changeCount"/>
      </label>
      <b-button @click="getFilteredReservations" :disabled="!isActive">
        Submit
      </b-button>
    </div>

    <ul class="list-unstyled">
      <b-media class='mb-3 title' tag="li" v-for="(el, index) in reservationsList" :key="index">
        <div class="title">

          <h5 class="mt-1">
            {{ el.id }}
            {{ el.tour.destination }}, {{ el.tour.date_from }} - {{ el.tour.date_to }}
          </h5>
          <router-link v-if="el" :to="'/reservations/' + el.id">
            <b-icon icon="arrow-right" style="width: 30px; height: 30px"></b-icon>
          </router-link>
        </div>
      </b-media>
    </ul>

    <v-pagination v-model="reservationsPagination.page"
                  :length="reservationsPagination.pages" @input="next"></v-pagination>
  </div>
</template>

<script>
import {mapGetters} from "vuex";

export default {
  name: "ReservationsPage",
  mounted() {
    this.$store.dispatch('getReservations')
  },
  data() {
    return {
      destination: null,
      count: null,
    }
  },
  computed: {
    ...mapGetters({
      reservationsList: 'reservationsList',
      reservationsPagination: 'reservationsPagination'
    }),
    isActive() {
       return !!(this.destination || this.count)
    },
    search() {
      return [this.destination, this.count].flatMap(el => el ? [el] : []).join(', ');
    }
  },
  methods: {
    next(page) {
      const payload = {
        page: page,
        search: this.search,
      }
      if (this.search) {
        this.$store.dispatch('getReservationsByCountDestination', payload)
      } else {
        this.$store.dispatch('getReservations', page);
      }
    },
    changeDestination(value) {
      this.destination = value
    },
    changeCount(value) {
      this.count = value
    },
    getFilteredReservations() {
      const payload = {
        search: this.search
      }
      this.$store.dispatch('getReservationsByCountDestination', payload)
    },
  }
}
</script>

<style scoped>
.title {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 20px;
}
</style>