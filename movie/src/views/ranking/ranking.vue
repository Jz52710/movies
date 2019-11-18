<template>
    <div class="ranking-box">
        排名
    </div>
</template>

<script>
    // @ is an alias to /src
    // import HelloWorld from '@/components/HelloWorld.vue'

    export default {
        name: 'ranking',
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
    .ranking-box{
        width: 100%;
        height: 100%;
    }
</style>
