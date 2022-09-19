<template>
  <b-col class="d-flex flex-column align-center mt-10">
    <Card :tourElement="reservation?.tour" is-reservation="true"/>
    <b-col cols="6">
      <b-card
          style="max-width: 30rem;"
          class="mb-2 mt-3"
      >
        <b-card-text>
          <h5>Детали заказа:</h5>
          <div class="mb-3">Человек: {{ reservation?.count }} </div>
          <div class="mb-3">
            <span>Подтверждение: </span>
            <input type="checkbox" :checked="reservation?.approved" disabled class="align-middle"/>
          </div>
          <p>Итоговая цена: {{ reservation?.tour?.price * reservation?.count}}</p>
          <b-button @click="cancel" class="btn-danger">Отменить</b-button>
        </b-card-text>
      </b-card>
    </b-col>
    <div style="margin-right: 90px">
      <router-link :to="`/leave_review/${$route.params.id}`">Рассказать о впечатлениях</router-link>
    </div>
  </b-col>
</template>

<script>
import {mapGetters} from "vuex";
import Card from "@/components/ToursPage/Card";

export default {
  name: "ReservationPage",
  mounted() {
    this.$store.dispatch('getReservation', this.$route.params.id)
  },
  methods: {
    cancel() {
      this.$store.dispatch('cancelReservation', this.reservation.id);
      this.$router.push('/');
    }
  },
  components: {Card},
  computed: {
    ...mapGetters({
      reservation: 'reservation',
    })
  },
}
</script>

<style scoped>

</style>