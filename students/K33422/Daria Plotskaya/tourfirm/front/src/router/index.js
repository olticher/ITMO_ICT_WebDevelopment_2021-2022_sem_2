import Vue from 'vue'
import VueRouter from 'vue-router'
import HomePage from '@/views/HomePage.vue'
import SignInPage from "@/views/auth/SignInPage";
import SignUpPage from "@/views/auth/SignUpPage";
import ToursPage from "@/views/ToursPage";
import HomeFilterPage from "@/views/HomeFilterPage";
import ReservationsPage from "@/views/ReservationsPage";
import ReservationPage from "@/views/ReservationPage";
import ReviewsPage from "@/views/ReviewsPage";
import LeaveReviewPage from "@/views/LeaveReviewPage";
import CreateReservationPage from "@/views/CreateReservationPage";

Vue.use(VueRouter)


const routes = [
    {
        path: '/',
        name: 'HomePage',
        component: HomePage
    },
    {
        path: '/tours_filter/',
        name: 'HomeFilterPage',
        component: HomeFilterPage
    },
    {
        path: '/tours/:id',
        name: 'ToursPage',
        component: ToursPage
    },
    {
        path: '/reservations/',
        name: 'ReservationsPage',
        component: ReservationsPage
    },
    {
        path: '/reservations/:id',
        name: 'ReservationPage',
        component: ReservationPage
    },
    {
        path: '/create_reservation/:id',
        name: 'CreateReservationPage',
        component: CreateReservationPage
    },
    {
        path: '/reviews/:id',
        name: 'Reviews',
        component: ReviewsPage
    },
    {
        path: '/leave_review/:id',
        name: 'LeaveReviewPage',
        component: LeaveReviewPage
    },

    {
        path: '/signin',
        name: 'SignIn',
        component: SignInPage
    },
    {
        path: '/signup',
        name: 'SignUp',
        component: SignUpPage
    },
]
const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

router.beforeEach((to, from, next) => {
    let isAuthenticated = localStorage.getItem('token');
    if (to.name !== 'SignIn' && to.name !== 'SignUp' && !isAuthenticated) next({name: 'SignIn'})
    else next()
})
export default router