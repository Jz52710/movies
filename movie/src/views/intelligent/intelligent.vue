<template>
    <div class="intelligent-box">
        智能推荐
    </div>
</template>

<script>
    // @ is an alias to /src
    // import HelloWorld from '@/components/HelloWorld.vue'

    export default {
        name: 'intelligent',
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
    .intelligent-box{
        width: 100%;
        height: 100%;
    }
</style>
