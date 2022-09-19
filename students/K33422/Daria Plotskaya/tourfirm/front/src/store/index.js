import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import router from "@/router";

import {retrievePagination} from "@/store/utils";

Vue.use(Vuex)

const instance = axios.create({
    baseURL: 'http://localhost:8000/api',
    timeout: 1000,
    headers: {'Content-Type': 'application/json',}
});

const instance2 = axios.create({
    baseURL: 'http://localhost:8000/api',
    timeout: 1000,
    headers: {'Content-Type': 'application/json',}
});

instance.interceptors.request.use(config => {
    config.headers.Authorization = `Bearer ${JSON.parse(localStorage.getItem('token'))?.access}`
    return config;
})

// instance.interceptors.response.use(
//     config => {
//         config.headers.Authorization = `Bearer ${JSON.parse(localStorage.getItem('token'))?.access}`
//         return config;
//     },
//     error => {
//         return Promise.reject(error)
//     }
// )

const store = new Vuex.Store({
    state: {
        id: null,
        username: '',
        toursList: [],
        tourElement: {},
        totalPrice: null,
        showComments: true,
        reservationsList: [],
        reservation: null,
        reviewsList: [],
        reviewError: '',
        reservationError: '',

        toursPagination: {
            next: '',
            prev: '',
            pages: 0,
            page: 0
        },

        reservationsPagination: {
            next: '',
            prev: '',
            pages: 0,
            page: 0
        },

        reviewsPagination: {
            next: '',
            prev: '',
            pages: 0,
            page: 0
        },
    },
    getters: {
        toursList(state) {
            return state.toursList
        },
        tourElement(state) {
            return state.tourElement
        },
        totalPrice(state) {
            return state.totalPrice
        },
        username(state) {
            return state.username
        },
        showComments(state) {
            return state.showComments
        },
        id(state) {
            return state.id
        },
        toursPagination(state) {
            return state.toursPagination
        },
        reservationsList(state) {
            return state.reservationsList
        },
        reservationsPagination(state) {
            return state.reservationsPagination
        },
        reservation(state) {
            return state.reservation
        },
        reviewsList(state) {
            return state.reviewsList
        },
        reviewsPagination(state) {
            return state.reviewsPagination
        },
        reviewError(state) {
            return state.reviewError
        },
        reservationError(state) {
            return state.reservationError
        },
    },
    mutations: {
        setUser(state, payload) {
            state.id = payload.id
            state.username = payload.username
        },
        setTours(state, payload) {
            state.toursList = payload
        },
        setTourElement(state, payload) {
            state.tourElement = payload
        },
        setTotalPrice(state, payload) {
            state.totalPrice = payload
        },
        setShowComments(state, payload) {
            state.showComments = payload
        },
        setToursPagination(state, payload) {
            state.toursPagination = payload
        },
        setReservations(state, payload) {
            state.reservationsList = payload
        },
        setReservationsPagination(state, payload) {
            state.reservationsPagination = payload
        },
        setReservation(state, payload) {
            state.reservation = payload
        },
        cancelReservation(state, payload) {
            state.reservation = null;
            const idx = state.reservationsList.findIndex(el => el.id === payload)
            state.reservationsList.splice(idx, 1);
        },
        setReviews(state, payload) {
            state.reviewsList = payload
        },
        setReviewsPagination(state, payload) {
            state.reviewsPagination = payload
        },
        setReviewError(state, payload) {
            state.reviewError = payload
        },
        setReservationError(state, payload) {
            state.reservationError = payload
        },
    },
    actions: {
        Register(store, payload) {
            instance2.post(`/auth/users/`, JSON.stringify(payload))
                .then(function(data) {
                    if (200 <= data.status < 300) {
                        return data.data;
                    }
                    return Promise.reject(data.status);
                })
                .then(function() {
                    store.dispatch('Login', {
                        username: payload.username,
                        password: payload.password,
                    })
                })
        },
        Login(store, payload) {
            instance.post(`/auth/jwt/create/`, JSON.stringify(payload))
                .then(function(data) {
                    if (200 <= data.status < 300) {
                        return data.data;
                    }
                    return Promise.reject(data.status);
                })
                .then(token => {
                    localStorage.setItem('token', JSON.stringify(token));
                    router.push('/')
                })
        },
        refresh() {
            instance.post(`/auth/jwt/refresh/`, {
                refresh: `${JSON.parse(localStorage.getItem('token'))?.access}`
            })
                .then(function(data) {
                    if (200 <= data.status < 300) {
                        return data.data;
                    }
                    return Promise.reject(data.status);
                })
                .then(token => {
                    localStorage.setItem('token', JSON.stringify(token));
                })
        },
        mountedProfile({commit}) {
            instance
                .get(`/auth/users/me/`)
                .then(function(data) {
                    if (200 <= data.status < 300) {
                        return data.data;
                    }
                    return Promise.reject(data.status);
                })
                .then(user => {
                    commit('setUser', {id: user.id, username: user.username})
                })
        },
        toursList({commit}, page) {
            instance.get(`/tours/`, {
                params: {
                    page: page
                }
            }).then(function(data) {
                if (200 <= data.status < 300) {
                    return data.data;
                }
                return Promise.reject(data);
            })
                .then(tours => {
                    const paginationData = retrievePagination(tours);
                    commit('setToursPagination', paginationData)
                    commit('setTours', tours.results)
                })
        },
        toursPriceRange({commit}, payload) {
            const {page, min, max, isSorted} = payload;
            instance.get(`/tours_price_range/`, {
                params: {
                    page: page,
                    price_min: min,
                    price_max: max,
                    ordering: isSorted ? 'price' : 'date_from'
                }
            }).then(function(data) {
                if (200 <= data.status < 300) {
                    return data.data;
                }
                return Promise.reject(data);
            })
                .then(tours => {
                    const paginationData = retrievePagination(tours);
                    commit('setToursPagination', paginationData)
                    commit('setTours', tours.results)
                })
        },
        toursElement({commit}, payload) {
            instance.get(`/tour/${payload}/`).then(function(data) {
                if (200 <= data.status < 300) {
                    return data.data;
                }
                return Promise.reject(data);
            })
                .then(tourElement => {
                    commit('setTourElement', tourElement)
                })
        },

        reservations({commit}, payload) {
            instance.post(`/reservations/`, JSON.stringify(payload)).then(function(data) {
                if (200 <= data.status < 300) {
                    return data.data;
                }
                return Promise.reject(data);
            })
                .then(data => {
                    commit('setTotalPrice', data.total_price)
                })
                .catch((e) => {
                    const {data} = e.response;
                    let msg = '';

                    if (data.reservation) msg += data.reservation
                    if (data.non_field_errors) msg += ' ' + data.non_field_errors[0]

                    commit('setReservationError', msg)
                })
        },
        getReservations({commit}, page) {
            instance.get(`/reservations/`, {
                params: {
                    page: page,
                }
            }).then(function(data) {
                if (200 <= data.status < 300) {
                    return data.data;
                }
                return Promise.reject(data);
            })
                .then(response => {
                    const paginationData = retrievePagination(response);
                    commit('setReservationsPagination', paginationData)
                    commit('setReservations', response.results)
                })
        },
        getReservationsByCountDestination({commit}, payload) {
            const {page, search} = payload;
            instance.get(`/reservations_search/`, {
                params: {
                    page: page,
                    search: search
                }
            }).then(function(data) {
                if (200 <= data.status < 300) {
                    return data.data;
                }
                return Promise.reject(data);
            })
                .then(response => {
                    const paginationData = retrievePagination(response);
                    commit('setReservationsPagination', paginationData)
                    commit('setReservations', response.results)
                })
        },
        getReservation({commit}, id) {
            instance.get(`/reservation/${id}/`).then(function(data) {
                if (200 <= data.status < 300) {
                    return data.data;
                }
                return Promise.reject(data);
            })
                .then(async response => {
                    const {data: tour} = await instance.get(`/tour/${response.tour}/`);
                    response.tour = tour;
                    commit('setReservation', response)
                })
        },
        cancelReservation({commit}, id) {
            instance.delete(`/reservation/${id}/`).then(function(data) {
                if (200 <= data.status < 300) {
                    return data.data;
                }
                return Promise.reject(data);
            })
                .then(response => {
                    commit('cancelReservation', response)
                })
        },
        getReviews({commit}, payload) {
            const {page, ordering, tour} = payload;
            instance.get(`/reviews_ordered/${tour}`, {
                params: {
                    page: page,
                    ordering: ordering,
                }
            }).then(function(data) {
                if (200 <= data.status < 300) {
                    return data.data;
                }
                return Promise.reject(data);
            })
                .then(response => {
                    const paginationData = retrievePagination(response);
                    const reviews = response.results;
                    commit('setReviewsPagination', paginationData)
                    commit('setReviews', reviews)
                })
        },
        createReview({commit}, payload) {
            instance.post(`/reviews/`, JSON.stringify(payload)).then(function(data) {
                if (200 <= data.status < 300) {
                    commit('setReviewError', '')
                    return data.data;
                }
                return Promise.reject(data);
            })
                .catch((e) => {
                    const {data} = e.response;
                    let msg = '';

                    if (data.reservation) msg += data.reservation
                    if (data.non_field_errors) msg += ' ' + data.non_field_errors[0]

                    commit('setReviewError', msg)
                })
        },
    }
})
export default store;
