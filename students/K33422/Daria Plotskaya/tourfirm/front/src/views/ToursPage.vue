<template>
  <main>
    <h2>Путевка в {{ tourElement.destination }}</h2>
    <b-container>
      <b-row class="d-flex">
        <Card :tourElement="tourElement"/>
        <b-col cols="6">
          <div style="height: 400px;">
            <div v-if="showComments" class="d-flex flex-column justify-center"
                 style=" height: 400px; align-items: center">
              <h5>Комментарии</h5>
              <div v-for="(el, index) in reviewsList.slice(0,2)" :key="index" style="max-height: 400px">
                <Comment2 :name="el.name" :text="el.text" :stars="el.stars"/>
              </div>
              <p v-if="!reviewsList.slice(0,2).length">
                Пока нет отзывов
              </p>
              <div class="mb-5" v-if="reviewsList.slice(0,2).length">
                <router-link :to="`/reviews/${$route.params.id}`">Все отзывы!</router-link>
              </div>
            </div>
          </div>
          <router-link :to="`/create_reservation/${$route.params.id}`">
            <b-button size="lg" variant="success">
              В путь!
            </b-button>
          </router-link>
        </b-col>
      </b-row>
      <div class="mt-5 mb-3">
        <b-carousel
            id="carousel-1"
            v-model="slide"
            :interval="4000"
            controls
            indicators
            background="#ababab"
            img-width="1024"
            img-height="480"
            style="text-shadow: 1px 1px 2px #333;"
            @sliding-start="onSlideStart"
            @sliding-end="onSlideEnd"
        >
          <b-carousel-slide
              caption="Best trip of your life....."
              text="Восхитительные пейзажи и незабываемые впечатления"
              img-src="https://picsum.photos/1024/480/?image=52"
          ></b-carousel-slide>
          <b-carousel-slide img-src="https://picsum.photos/1024/480/?image=54">
            <h1>{{ tourElement.destination }}</h1>
          </b-carousel-slide>
          <b-carousel-slide img-src="https://picsum.photos/1024/480/?image=58"></b-carousel-slide>
          <b-carousel-slide>
            <template #img>
              <img
                  class="d-block img-fluid w-100"
                  width="1024"
                  height="480"
                  src="https://picsum.photos/1024/480/?image=55"
                  alt="image slot"
              >
            </template>
          </b-carousel-slide>
        </b-carousel>
      </div>
    </b-container>
  </main>
</template>

<script>
import {mapGetters} from "vuex";
import Card from "@/components/ToursPage/Card";
import Comment2 from "@/components/ToursPage/Comment2";

export default {
  name: "ToursPage",
  components: {Comment2, Card},
  data() {
    return {
      slide: 0,
      sliding: null
    }
  },
  mounted() {
    this.$store.dispatch('toursElement', this.$route.params.id)
    this.$store.dispatch('getReviews', {page: 1, tour: this.$route.params.id})
    // console.log(this.reviewsList);
  },
  methods: {
    show(flag) {
      this.$store.commit('setShowComments', flag)
    },
    onSlideStart() {
      this.sliding = true
    },
    onSlideEnd() {
      this.sliding = false
    },
  },
  computed: {
    ...mapGetters({
      tourElement: 'tourElement',
      showComments: 'showComments',
      reviewsList: 'reviewsList'
    })
  },
}
</script>

<style scoped>

</style>