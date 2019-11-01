import { goGet, goPost, goDelete, goPut, goPatch } from './axios'

export const getBatchList = (params) => goGet('/admin/api/jobsExecuteLog/list', params)// 获取批次管理列表

export const deleteBatch = (params) => goPost('/admin/api/jobsExecuteLog/delete?', params)// 删除单个批次

export const delBatchs = (params) => goPost('/admin/api/jobsExecuteLog/bulkDel', params)// 批量删除批次

export const getTaskList = (params) => goGet('/admin/api/urlsExecuteLog/list', params)// 获取任务管理列表

export const deleteTask = (params) => goPost('/admin/api/urlsExecuteLog/delete?', params)// 删除单个任务

export const delTasks = (params) => goPost('/admin/api/urlsExecuteLog/bulkDel', params)// 批量删除任务

export const runTask = (params) => goPost('/nservice/store/excuteTaskNow', params)// 重跑任务

export const getPictureList = (params) => goGet('/admin/api/urlsImagesPath/list', params)// 获取图片管理列表

export const deletePicture = (params) => goPost('/admin/api/urlsImagesPath/delete?', params)// 删除单个图片

export const delPictures = (params) => goPost('/admin/api/urlsImagesPath/bulkDel', params)// 批量删除图片

export const getPicClass = (params) => goGet('/admin/api/urlsImagesPath/list', params, { showLoading: false })// 获取类目列表

export const getStoreList = (params) => goGet('/admin/api/screenShotUrls/list', params)// 获取店铺管理列表

export const deleteStore = (params) => goPost('/admin/api/screenShotUrls/delete?', params)// 删除单个店铺

export const delStores = (params) => goPost('/admin/api/screenShotUrls/bulkDel', params)// 批量删除店铺

export const getStoreClass = (params) => goGet('/nservice/store/getStoreClass', params, { showLoading: false })// 获取店铺所属类目列表

export const _editTitle = (params) => goPut('/nservice/store/updateStoreTitle', params, { showLoading: false })// 修改店铺名称

export const _editClass = (params) => goPut('/nservice/store/updateStoreClass', params, { showLoading: false })// 获取店铺所属类目列表

export const _editUrl = (params) => goPut('/nservice/store/updateStoreUrl', params, { showLoading: false })// 获取店铺所属类目列表
