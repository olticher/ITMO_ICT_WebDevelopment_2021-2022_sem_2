<template>
  <b-col>
    <h1 class="mt-10">Оставить отзыв</h1>
    <form @submit.prevent="onSubmit(form)" class="form-container">
      <div class="mb-3">
        <label for="input-default" class="mb-3"/>
        <b-form-textarea v-model="form.text" id="input-default" placeholder="Ваш комментарий"
                         style="width: 500px"></b-form-textarea>
      </div>
      <div class="mb-3">
        <label for="input-default" class="mr-5">Оценка:</label>
        <v-select v-model="form.stars" :items="options" id="input-default" style="width: 100px"></v-select>
      </div>
      <b-button type="submit" variant="outline-primary" :disabled="!isActive">Опубликовать!</b-button>
      <p v-if="reviewError" style="color: darkred">{{ reviewError }}</p>
    </form>
  </b-col>
</template>

<script>
import {mapGetters} from "vuex";

export default {
  name: "LeaveReviewPage",
  data() {
    return {
      form: {
        reservation: this.$store.state.reservation.id,
        text: '',
        stars: '',
      },
      options: [...Array(10).keys()].map((el) => ({
        value: el + 1,
        text: el + 1
      }))
    }
  },
  mounted() {
    console.log('reserv', this.$store.state.reservation.id)
  },
  destroyed() {
    this.$store.commit('setReviewError', null)
  },
  methods: {
    onSubmit(form) {
      this.$store.dispatch('createReview', form)
    }
  },
  computed: {
    ...mapGetters({
      reviewError: 'reviewError',
    }),
    isActive() {
      return !!(this.form.text && this.form.stars)
    },
  },
}
</script>

<style scoped>
.form-container {
  margin-top: 100px;
  width: 100%;
  min-height: 330px;
  padding: 20px;
  text-align: start;
  border: 1px solid rgba(0, 0, 0, 0.22);
  border-radius: 4px;
  background: rgba(186, 186, 186, 0.19);
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10px;
}
</style>