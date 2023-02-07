<script setup lang="ts">
import { ref } from 'vue'

const props = defineProps({
  src: {
    type: String,
  },
  alt: {
    type: String,
  },
  width: {
    type: String,
  },
  caption: {
        type: String,
  },
  url: {
      type: String,
  },
})

const image = ref(props.src)
</script>

<template>
  <div>
    <img :width="props.width" :alt="props.alt" :src="props.src"/>
  </div>
  <div v-if="props.caption" class="rel-b m-2 pl-2 text-sm opacity-70">
      <a v-if="props.url" :href="props.url" target="_blank" class="text-lg icon-btn opacity-70 !border-none !hover:text-gray"><mdi-open-in-new/></a> <span v-html="props.caption"></span> 
  </div>
</template>
