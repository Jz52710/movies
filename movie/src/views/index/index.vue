<template>
    <div class="index-box">
        <el-container>
            <el-header>
                <Header></Header>
            </el-header>
            <el-main>
                <router-view></router-view>
            </el-main>
        </el-container>
    </div>
</template>

<script>
    // @ is an alias to /src
    // import HelloWorld from '@/components/HelloWorld.vue'
    import Header from '@/components/header/header.vue'

    export default {
        name: 'index',
        components: {
            // HelloWorld
            Header
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
    .index-box{
        width: 100%;
        height: 100%;
    }
    .el-container{
        width: 100%;
        height: 100%;
    }
    .el-header{
        background-color: #e3ebec;
        color: #333;
        text-align: center;
        line-height: 60px;
    }
    .el-main {
        background-color: white;
        color: #333;
        text-align: center;
        line-height: 160px;
        padding: 0!important;
    }
    .left-box{
        font-weight: 600;
        font-size: 24px;
    }
    .right-box{
        float: right;
    }

</style>
