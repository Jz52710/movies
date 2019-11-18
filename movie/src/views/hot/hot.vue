<template>
    <div class="hot-box">
       正在热映
    </div>
</template>

<script>
    // @ is an alias to /src
    // import HelloWorld from '@/components/HelloWorld.vue'

    export default {
        name: 'hot',
        components: {
            // HelloWorld
        },
        data(){
            return {
                activeIndex: '1'
            }
        },
        methods: {
            handleSelect() {
            }
        }
    }
</script>
<style>
    .hot-box{
        width: 100%;
        height: 100%;
    }
</style>
