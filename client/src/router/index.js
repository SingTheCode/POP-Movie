import Vue from "vue";
import VueRouter from "vue-router";

import BoxOfficeView from "@/views/BoxOfficeView";
import MovieDaysView from "@/views/MovieDaysView";
import MovieDetailView from "@/views/MovieDetailView";
import MyPageView from "@/views/MyPageView";
import NotFound from "../views/NotFound.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "BoxOffice",
    component: BoxOfficeView,
  },
  {
    path: "/movie/:id",
    name: "MovieDetail",
    component: MovieDetailView,
  },
  {
    path: "/moviedays",
    name: "MovieDays",
    component: MovieDaysView,
  },
  {
    path: "/mypage",
    name: "MyPage",
    component: MyPageView,
  },
  {
    path: "/notfound",
    name: "NotFound",
    component: NotFound,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

// 라우터 가드!
router.beforeEach((to, from, next) => {
  // 로그를 찍으면 이동 위치를 알 수 있습니다.
  // console.log(to.name);

  // 3항 연산자 응용
  !to.name ? next({ name: "NotFound" }) : next();

  // 이렇게 작성 하셔도 됩니다.
  // if (!to.name) {
  //   next({ name: 'NotFound' })
  // }
  // next()
});

export default router;
