import { goGet, goPost, goDelete, goPut, goPatch } from './axios'

// 账号管理
export const getUserInfo = (params) => goGet('/user/query', params)// 获取用户信息

export const getUserInfoP = (params) => goPost('/user/pagingquery', params)// 获取用户信息(分页)

export const addUser = (params) => goPost('/user/save', params)// 新增用户

export const disableUser = (params) => goPost('/user/disable', params)// 禁用用户

export const enableUser = (params) => goPost('/user/enable', params)// 启用用户

export const userStatus = (params) => goGet('/user/status/query', params)// 账号状态查询

// 用户店铺关联（添加权限/编辑权限）

export const userShopDelete = (params) => goDelete('/usershop/delete', params)// 删除用户店铺关联信息

export const userShopQuery = (params) => goGet('/usershop/query', params)// 查询用户店铺关联信息（编辑）

export const userShopQueryAll = (params) => goGet('/usershop/user/query', params)// 查询用户店铺关联信息(全部)

export const userShopSave = (params) => goPost('/usershop/save', params)// 新增或更新用户店铺关联信息

// 部门信息

export const departmentQuery = (params) => goPost('/department/query', params, { showLoading: false })// 新增或更新用户店铺关联信息

// APP操作接口（应用平台）
export const appQuery = (params) => goPost('/app/query', params, { showLoading: false, showMessage: true })// 新增或更新用户店铺关联信息

// 运营组列表、店铺列表 模糊搜索
export const opersGroupQuery = (params) => goPost('/opDomain/query', params, { showLoading: false })// 运营组查询

export const shopQuery = (params) => goPost('/shop/query', params, { showLoading: false })// 模糊搜索运营组

// 运营组操作
export const allOpersGroupList = (params) => goPost('/opDomain/all/query', params)// 获取运营组列表

export const getOpersGroupList = (params) => goPost('/opDomain/query', params)// 获取运营组列表

export const addOpersGroup = (params) => goPost('/opDomain/save', params)// 添加运营组

export const enableOpersGroup = (params) => goPost('/opDomain/enable', params)// 启用运营组

export const deleteOpersGroup = (params) => goPost('/opDomain/delete', params)// 禁用运营组

export const updateOpersGroup = (params) => goPost('/opDomain/update', params)// 更新运营组

export const OpersGroupStatus = (params) => goGet('/opDomain/status/query', params)// 运营组状态查询

// 店铺列表
export const getPlatforms = (params) => goPost('/platform/getplatform', params, { showLoading: false, showMessage: true })

export const batchdeleteShop = (params) => goPost('/shop/batchdelete', params, { showLoading: false, showMessage: true })

export const getShopList = (params) => goPost('/shop/query', params) // 店铺查询

export const saveShop = (params) => goPost('/shop/save', params, { showLoading: false, showMessage: true })// 新增或编辑店铺

export const enableShop = (params) => goPost('/shop/enable', params, { showLoading: false, showMessage: true })

export const deleteShop = (params) => goPost('/shop/delete', params, { showLoading: false, showMessage: true })

export const getShopStatus = (params) => goGet('/shop/status/query', params, { showLoading: false, showMessage: true }) // 店铺状态查询

export const getShopUser = (params) => goPost('/usershop/shop/query', params) // 查看店铺列表及运营组列表的授权用户信息

export const getUserStatus = (params) => goGet('/user/status/query', params, { showLoading: false, showMessage: true })

export const getDepartment = (params) => goPost('/department/query', params, { showLoading: false, showMessage: true })

export const getApps = (params) => goPost('/app/query', params, { showLoading: false, showMessage: true })

export const getEnableStatus = (params) => goGet('/shop/enable/query', params, { showLoading: false, showMessage: true })// 查询店铺状态

// bu查询
export const buQuery = (params) => goPost('/bu/query', params, { showLoading: false, showMessage: true })
// 账号类型查询
export const userTypeQuery = (params) => goGet('/user/type', params, { showLoading: false, showMessage: true })

// dashboard
export const getDashboardAPP = (params) => goGet(`${process.env.VUE_APP_DASBOARD_SERVER}/dashboard/kpi/query`, params, { showLoading: true, showMessage: true })
export const getDashboardModel = (params) => goGet(`${process.env.VUE_APP_DASBOARD_SERVER}/dashboard/kpi/query`, params, { showLoading: false, showMessage: true })
export const getDashboardTarget = (params) => goGet(`${process.env.VUE_APP_DASBOARD_SERVER}/dashboard/kpi/query`, params, { showLoading: false, showMessage: true })
