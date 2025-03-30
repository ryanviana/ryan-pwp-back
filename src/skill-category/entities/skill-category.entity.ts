import { Prop, Schema, SchemaFactory } from '@nestjs/mongoose';
import { HydratedDocument } from 'mongoose';

export type SkillCategoryDocument = HydratedDocument<SkillCategory>;

@Schema({ timestamps: true })
export class SkillCategory {
  @Prop({ required: true })
  name: string;

  @Prop({ type: [String], required: true })
  skills: string[];
}

export const SkillCategorySchema = SchemaFactory.createForClass(SkillCategory);
