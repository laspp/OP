<script setup lang="ts">
import { computed } from 'vue';
import { handleBackground } from '@slidev/theme-default/layoutHelper';
const props = defineProps({
	image: {
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
});
const style = computed(() => handleBackground(props.image));
</script>

<template>
	<div class="slidev-layout h-full w-full" :style="style">

		<slot :class="props.class"/>

		<div v-if="props.caption" class="fixed bottom-0 left-0 bg-black bg-opacity-50 text-sm m-2 py-1 px-3 text-shadow-xl">
            <a v-if="props.url" :href="props.url" target="_blank" class="text-lg icon-btn opacity-70 !border-none !hover:text-gray"><mdi-open-in-new/></a> <span v-html="props.caption"></span> 
        </div>

	</div>
</template>