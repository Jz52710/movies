<template>
    <div class="header-box">
        <el-row :span="24">
            <el-col :span="4" class="left-box">
                iMovies
            </el-col>
            <el-col :span="6" class="right-box">
                <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect" background-color="#e3ebec" active-text-color="#409EFF" style="display:flex;">
                    <el-menu-item index="1">
                        <router-link :to="{name:'intelligent'}" tag="div" style="width: 96px;">
                            智能推荐
                        </router-link>
                    </el-menu-item>
                    <el-menu-item index="2">
                        <router-link :to="{name:'classify'}" tag="div" style="width: 96px;">
                            分类
                        </router-link>
                    </el-menu-item>
                    <el-menu-item index="3">
                        <router-link :to="{name:'ranking'}" tag="div" style="width: 96px;">
                            TOP250
                        </router-link>
                    </el-menu-item>
                    <el-menu-item index="4">
                        <router-link :to="{name:'hot'}" tag="div" style="width: 96px;">
                            正在热映
                        </router-link>
                    </el-menu-item>


                </el-menu>

            </el-col>
        </el-row>
        <el-main>
            <router-view></router-view>
        </el-main>
    </div>
</template>

<script>
    // @ is an alias to /src
    // import HelloWorld from '@/components/HelloWorld.vue'

    export default {
        name: 'headers',
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
    .header-box{
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
    }
    .left-box{
        font-weight: 600;
        font-size: 24px;
    }
    .right-box{
        float: right;
        display: flex;
    }
    .el-menu--horizontal{
        border: none!important;
    }
    .el-menu-item{
        padding: 0!important;
    }
</style>
