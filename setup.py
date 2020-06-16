# coding=utf-8

from distutils.core import setup
setup(
  name = 'kalasearch',         
  packages = ['kalasearch'],   
  version = '0.0.3',      
  license='MIT',        
  description = '卡拉搜索SDK-五分钟帮你打造站内、app内搜索引擎，适用于APP、小程序、电商、软件服务等领域',   
  author = 'Eddie Xie',                 
  author_email = 'oeddyo@gmail.com',    
  url = 'https://kalasearch.cn',
  download_url = 'https://github.com/oeddyo/kalasearch-python-sdk/archive/0.0.3.tar.gz',    # I explain this later on
  keywords = ['搜索', '后端', '中台', 'search', 'full-text search', '搜索引擎', '站内搜索'],   
  install_requires=[            
          'requests',
      ],
  classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
  ],
  include_package_data=True,
  python_requires=">=3"
)
