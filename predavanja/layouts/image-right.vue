<script setup lang="ts">
import { computed, defineProps } from 'vue';
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
	<div class="h-full w-full">

		<div class="grid grid-cols-2 w-full h-full">
			<div class="slidev-layout default mt-4 h-auto" :class="props.class">
				<slot />
			</div>
			<div class="slidev-layout w-full h-full" :style="style">
                <div class="fixed bottom-0 right-0 bg-black bg-opacity-50 text-sm m-2 py-1 px-3 text-shadow-xl">
                    <a v-if="props.url" :href="props.url" target="_blank" class="text-lg icon-btn opacity-70 !border-none !hover:text-gray"><mdi-open-in-new/></a> <span v-html="props.caption"></span>
                </div>
            </div>
		</div>
		
	</div>
</template>