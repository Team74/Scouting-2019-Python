# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mysqlx_expect.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='mysqlx_expect.proto',
  package='Mysqlx.Expect',
  syntax='proto2',
  serialized_pb=_b('\n\x13mysqlx_expect.proto\x12\rMysqlx.Expect\"\xd0\x03\n\x04Open\x12\x42\n\x02op\x18\x01 \x01(\x0e\x32 .Mysqlx.Expect.Open.CtxOperation:\x14\x45XPECT_CTX_COPY_PREV\x12+\n\x04\x63ond\x18\x02 \x03(\x0b\x32\x1d.Mysqlx.Expect.Open.Condition\x1a\x96\x02\n\tCondition\x12\x15\n\rcondition_key\x18\x01 \x02(\r\x12\x17\n\x0f\x63ondition_value\x18\x02 \x01(\x0c\x12K\n\x02op\x18\x03 \x01(\x0e\x32\x30.Mysqlx.Expect.Open.Condition.ConditionOperation:\rEXPECT_OP_SET\"N\n\x03Key\x12\x13\n\x0f\x45XPECT_NO_ERROR\x10\x01\x12\x16\n\x12\x45XPECT_FIELD_EXIST\x10\x02\x12\x1a\n\x16\x45XPECT_DOCID_GENERATED\x10\x03\"<\n\x12\x43onditionOperation\x12\x11\n\rEXPECT_OP_SET\x10\x00\x12\x13\n\x0f\x45XPECT_OP_UNSET\x10\x01\">\n\x0c\x43txOperation\x12\x18\n\x14\x45XPECT_CTX_COPY_PREV\x10\x00\x12\x14\n\x10\x45XPECT_CTX_EMPTY\x10\x01\"\x07\n\x05\x43loseB\x1b\n\x17\x63om.mysql.cj.x.protobufH\x03')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_OPEN_CONDITION_KEY = _descriptor.EnumDescriptor(
  name='Key',
  full_name='Mysqlx.Expect.Open.Condition.Key',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='EXPECT_NO_ERROR', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXPECT_FIELD_EXIST', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXPECT_DOCID_GENERATED', index=2, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=299,
  serialized_end=377,
)
_sym_db.RegisterEnumDescriptor(_OPEN_CONDITION_KEY)

_OPEN_CONDITION_CONDITIONOPERATION = _descriptor.EnumDescriptor(
  name='ConditionOperation',
  full_name='Mysqlx.Expect.Open.Condition.ConditionOperation',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='EXPECT_OP_SET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXPECT_OP_UNSET', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=379,
  serialized_end=439,
)
_sym_db.RegisterEnumDescriptor(_OPEN_CONDITION_CONDITIONOPERATION)

_OPEN_CTXOPERATION = _descriptor.EnumDescriptor(
  name='CtxOperation',
  full_name='Mysqlx.Expect.Open.CtxOperation',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='EXPECT_CTX_COPY_PREV', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXPECT_CTX_EMPTY', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=441,
  serialized_end=503,
)
_sym_db.RegisterEnumDescriptor(_OPEN_CTXOPERATION)


_OPEN_CONDITION = _descriptor.Descriptor(
  name='Condition',
  full_name='Mysqlx.Expect.Open.Condition',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='condition_key', full_name='Mysqlx.Expect.Open.Condition.condition_key', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='condition_value', full_name='Mysqlx.Expect.Open.Condition.condition_value', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='op', full_name='Mysqlx.Expect.Open.Condition.op', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _OPEN_CONDITION_KEY,
    _OPEN_CONDITION_CONDITIONOPERATION,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=161,
  serialized_end=439,
)

_OPEN = _descriptor.Descriptor(
  name='Open',
  full_name='Mysqlx.Expect.Open',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='op', full_name='Mysqlx.Expect.Open.op', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cond', full_name='Mysqlx.Expect.Open.cond', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_OPEN_CONDITION, ],
  enum_types=[
    _OPEN_CTXOPERATION,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=39,
  serialized_end=503,
)


_CLOSE = _descriptor.Descriptor(
  name='Close',
  full_name='Mysqlx.Expect.Close',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=505,
  serialized_end=512,
)

_OPEN_CONDITION.fields_by_name['op'].enum_type = _OPEN_CONDITION_CONDITIONOPERATION
_OPEN_CONDITION.containing_type = _OPEN
_OPEN_CONDITION_KEY.containing_type = _OPEN_CONDITION
_OPEN_CONDITION_CONDITIONOPERATION.containing_type = _OPEN_CONDITION
_OPEN.fields_by_name['op'].enum_type = _OPEN_CTXOPERATION
_OPEN.fields_by_name['cond'].message_type = _OPEN_CONDITION
_OPEN_CTXOPERATION.containing_type = _OPEN
DESCRIPTOR.message_types_by_name['Open'] = _OPEN
DESCRIPTOR.message_types_by_name['Close'] = _CLOSE

Open = _reflection.GeneratedProtocolMessageType('Open', (_message.Message,), dict(

  Condition = _reflection.GeneratedProtocolMessageType('Condition', (_message.Message,), dict(
    DESCRIPTOR = _OPEN_CONDITION,
    __module__ = 'mysqlx_expect_pb2'
    # @@protoc_insertion_point(class_scope:Mysqlx.Expect.Open.Condition)
    ))
  ,
  DESCRIPTOR = _OPEN,
  __module__ = 'mysqlx_expect_pb2'
  # @@protoc_insertion_point(class_scope:Mysqlx.Expect.Open)
  ))
_sym_db.RegisterMessage(Open)
_sym_db.RegisterMessage(Open.Condition)

Close = _reflection.GeneratedProtocolMessageType('Close', (_message.Message,), dict(
  DESCRIPTOR = _CLOSE,
  __module__ = 'mysqlx_expect_pb2'
  # @@protoc_insertion_point(class_scope:Mysqlx.Expect.Close)
  ))
_sym_db.RegisterMessage(Close)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\027com.mysql.cj.x.protobufH\003'))
# @@protoc_insertion_point(module_scope)
