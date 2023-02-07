<script setup lang="ts">
import { computed } from "vue"

const props = defineProps({
    bgcolor: {
    type: String,
  },
  completed: {
    type: Number,
    default: 0,
  },
  total: {
    type: Number,
    default: 13
  },
})

const fillerStyles = computed(() => {
    const percents = props.completed/props.total * 100;
    return {
    height: "100%",
    width: `${percents}%`,
    backgroundColor: props.bgcolor,
    transition: "width 1s ease-in-out",
    borderRadius: "inherit",
    textAlign: "center",
};
});
</script>

<template>
<div class="container-bar">
    <div :style="fillerStyles">
    <span class="text-white text-sm p-0">{{ completed }}</span>
    </div>
</div>
</template>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.container-bar {
width: 868px;
background-color: #f0f0f0;
border-radius: 50px;
margin: 10px auto;
position: absolute;
top: 0px;
}
</style>
  