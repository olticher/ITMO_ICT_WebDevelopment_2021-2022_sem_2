<template>
  <b-col cols="6">
    <b-card
        title=""
        img-src="https://picsum.photos/600/300/?image=25"
        img-alt="Image"
        img-top
        tag="article"
        style="max-width: 30rem;"
        class="mb-2 mt-3"
    >
      <b-card-text>
        <h5> {{ tourElement.destination }}</h5>
        <p>Даты: {{ tourElement.date_from }} - {{ tourElement.date_to }}</p>
        <p>Отель: {{ tourElement.hotel }}</p>
        <p>Цена: {{ tourElement.price }}</p>
      </b-card-text>

      <div v-if="!isReservation">
        <b-button v-if="!showComments" @click="show(true)" variant="primary">Посмотреть отзывы</b-button>
        <b-button v-else @click="show(false)" variant="primary">Скрыть отзывы</b-button>
      </div>
    </b-card>
  </b-col>
</template>

<script>
import {mapGetters} from "vuex";

export default {
  name: "Card",
  props: ['tourElement', 'isReservation'],
  methods: {
    show(flag) {
      this.$store.commit('setShowComments', flag)
    }
  },
  computed: {
    ...mapGetters({
      showComments: 'showComments',
    })
  },
}
</script>

<style scoped>

</style>