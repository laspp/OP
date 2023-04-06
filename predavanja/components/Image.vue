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
  class: {
      type: String,
  },
})

const image = ref(props.src)
</script>

<template>  
  <div :class="props.class">
    <div>
      <img :width="props.width" :alt="props.alt" :src="props.src"/>
    </div>
    <div v-if="props.caption" class="rel-b m-2 pl-2 text-sm opacity-70">
        <span v-html="props.caption"></span>
        <span v-if="props.url">&nbsp;</span>
        <a v-if="props.url" :href="props.url" target="_blank" class="text-xs opacity-70">[vir]</a>
    </div>
  </div>
</template>
