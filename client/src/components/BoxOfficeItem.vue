<template>
  <div id="box-office-item">
    <div id="rank">{{ boxOfficeItem.rank }}</div>
    <div id="title">{{ boxOfficeItem.title }}</div>
    <div id="release-date">{{ boxOfficeItem.releaseDate }}</div>
    <div id="max-theather">{{ boxOfficeItem.screenNum }}</div>
    <div id="gross">{{ boxOfficeItem.spectatorNum }}</div>
    <button>Details</button>
  </div>
</template>

<script>
export default {
  name: "BoxOfficeItem",
  props: {
    boxOfficeItem: {
      rank: Number,
      title: String,
      releaseDate: String,
      screenNum: Number,
      spectatorNum: Number,
    },
  },
};
</script>

<style scoped></style>
