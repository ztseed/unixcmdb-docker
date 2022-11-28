grant all privileges on unixcmdb.* to 'ztseed'@'%';
flush privileges;
use unixcmdb;
source /dump/nnitcmdb_20220822.sql;

