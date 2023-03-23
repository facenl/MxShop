## MxShop
### 技术栈Vue+DRF

#### nodejs 版本 建议14
#### 进入跟目录 执行如下两条命令

```javascript
cnpm install
cnpm run dev
```
localhost:8080

Django
初始化项目
名称MxShop

根目录下创建apps -- 用于存放多个app
并在settings中添加如下
```python
sys.path.insert(0, BASE_DIR)
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
```