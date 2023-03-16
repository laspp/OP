<!--
  Usage:

```md
---
layout: two-cols-title
title: 'Level 1 common title'
---

# Left

This shows on the left

::right::

# Right

This shows on the right
```

-->

<script setup lang="ts">
const props = defineProps({
  class: {
    type: String,
  },
})
</script>

<template>
  <div class="slidev-layout">   
    <slot name="title"/> 
    
    <div class="two-columns w-full grid grid-cols-2 gap-x-10">
      <div class="col-left" :class="props.class">
        <slot name="left"/>
      </div>
      <div class="col-right" :class="props.class">
        <slot name="right" />
      </div>
    </div>
  </div>
  
</template>