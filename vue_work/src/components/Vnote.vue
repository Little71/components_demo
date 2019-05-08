<template>
  <div class="container">
    <div class="row">
      <div class="col-md-3">
        <div class="panel panel-default">
          <div class="panel-heading">
            <h3 class="panel-title">笔记列表</h3>
          </div>
          <div class="panel-body">
            <!-- 笔记列表 -->
            <VnoteShow></VnoteShow>
          </div>
        </div>
      </div>
      <div class="col-md-9">
        <!-- markdown编辑器 -->
        <div class="panel panel-default">
          <div class="panel-heading">
            
          </div>
          <div class="panel-body">
               <Vmark></Vmark>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import Vmark from './Vmark';
import VnoteShow from './VnoteShow';
export default {
    name:'Vnote',
    data(){
        return{}
    },
    components:{
        Vmark,
        VnoteShow,
    }
}
</script>
<style>

</style>
