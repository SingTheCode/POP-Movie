<template>
  <div id="comment-list">
    <comment-item
        v-for="comment in commentList"
        :userId="comment.userId"
        :context="comment.context"
        :key="comment.id"
    >
    </comment-item>
  </div>
</template>

<script>
import {mapGetters} from "vuex";

import CommentItem from "@/components/CommentItem";

export default {
  name: "CommentList",
  components: {
    CommentItem,
  },
  computed: {
    ...mapGetters(['commentList']),
  },
};
</script>

<style scoped>
#comment-list {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
}
</style>
